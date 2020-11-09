import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def propertyInteractionDF():
    property_interaction_df = pd.DataFrame(
        pd.read_csv("collaborativefiltering/dataset_interaction_excel.csv", index_col=0)
    )
    return property_interaction_df


def interactionMatrix():
    property_interaction_df = propertyInteractionDF()
    interactions_matrix = pd.pivot_table(
        property_interaction_df,
        values="ratings",
        index="user_id",
        columns="property_id",
        aggfunc=np.max,
    ).fillna(0)
    return interactions_matrix


def postData(data):
    property_interaction_df = propertyInteractionDF()
    if (data["user_id"] in property_interaction_df.index) and (
        data["property_id"] in property_interaction_df.values
    ):
        cekBool = False
        for cek in property_interaction_df.loc[data["user_id"]].values:
            print(cek)
            print(cek[0])
            print(data["property_id"])
            print(cek[1])
            print(data["ratings"])
            if (cek[0] == data["property_id"]) and (cek[1] == data["ratings"]):
                cekBool = True
        if cekBool:
            pass
        else:
            file = open("collaborativefiltering/dataset_interaction_excel.csv", "a")
            file.write(
                data["user_id"] + "," + data["property_id"] + "," + str(data["ratings"])
            )
            file.write("\n")
            file.close()
    else:
        file = open("collaborativefiltering/dataset_interaction_excel.csv", "a")
        file.write(
            data["user_id"] + "," + data["property_id"] + "," + str(data["ratings"])
        )
        file.write("\n")
        file.close()
    return 0


def new_user():
    property_interaction_df = propertyInteractionDF()
    list = []
    for i in range(50):
        list.append(property_interaction_df.property_id.value_counts().index[i])
    return list


def similar_users(user_id, interactions_matrix):
    similarity = []
    for user in range(0, interactions_matrix.shape[0]):
        sim = cosine_similarity(
            [interactions_matrix.loc[user_id]],
            [interactions_matrix.loc[interactions_matrix.index[user]]],
        )
        similarity.append((interactions_matrix.index[user], sim))
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_users = [tup[0] for tup in similarity]
    similarity_score = [tup[1] for tup in similarity]
    most_similar_users.remove(user_id)
    similarity_score.remove(similarity_score[0])
    return most_similar_users, similarity_score


def recommendations(user_id, num_of_property, user_item_interactions):
    most_similar_users = similar_users(user_id, user_item_interactions)[0]
    property_ids = set(
        list(
            user_item_interactions.columns[
                np.where(user_item_interactions.loc[user_id] > 0)
            ]
        )
    )
    recommendations = []
    already_interacted = property_ids.copy()
    for similar_user in most_similar_users:
        if len(recommendations) < num_of_property:
            similar_user_property_ids = set(
                list(
                    user_item_interactions.columns[
                        np.where(user_item_interactions.loc[similar_user] > 0)
                    ]
                )
            )
            recommendations.extend(
                list(similar_user_property_ids.difference(already_interacted))
            )
            already_interacted = already_interacted.union(similar_user_property_ids)
        else:
            break
    return recommendations[:num_of_property]
