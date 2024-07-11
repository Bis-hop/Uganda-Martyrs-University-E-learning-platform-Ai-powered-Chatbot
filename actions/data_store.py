# import pandas as pd
# import os


# def DataStore(name, email,):
#     if os.path.isfile("user_data.xlsx"):
#         df = pd.read_excel("user_data.xlsx")
#         df = df.append(pd.DataFrame([[name, email, ]],
#                                     columns=["name", , "email",]))
#         df.to_excel("user_data.xlsx", index=False)
#     else:
#         df = pd.DataFrame([[name, email]], 
# columns=["name", "email"])
#         df.to_excel("user_data.xlsx", index=False)
#         return []

# New
# import pandas as pd
# import os


# def DataStore(name, email):
#     file_path = "user_data.xlsx"
#     if os.path.isfile(file_path):
#         df = pd.read_excel(file_path)
#         new_data = pd.DataFrame([[name, email]], columns=["name", "email"])
#         df = pd.concat([df, new_data], ignore_index=True)
#         df.to_excel(file_path, index=False)
#     else:
#         df = pd.DataFrame([[name, email]], columns=["name", "email"])
#         df.to_excel(file_path, index=False)
