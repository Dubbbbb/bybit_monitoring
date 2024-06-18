from sqladmin import ModelView
from src.database.models import ExampleModel


class ExampleAdmin(ModelView, model=ExampleModel):
    pass


# class ExampleAdmin(ModelView, model=ExampleModel):
#     column_list = [ExampleModel.id, ExampleModel.name]
#     name_plural = "Пользователи"
#     name = "Пользователь"
#     icon = "fa-solid fa-user"
#
#     column_labels = {
#         ExampleModel.id: "ID",
#         ExampleModel.name: "Имя",
#     }
#
#     column_details_exclude_list = [
#         ExampleModel.password
#     ]
#
#     form_excluded_columns = [
#         ExampleModel.password
#     ]
