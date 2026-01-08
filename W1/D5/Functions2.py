# "Args and **Kwargs

# def say_hello(language, user_name):
#     if language == "EN":
#         print(f"Hello, {user_name}")
#
# say_hello()
#
# def print_names(*args):
#     for name in args:
#         print(f"Hello, {name}")
#     if not args:
#         print("Please add a name to say hello")
#
# print_names("Julia", "Avner", 1, "Duka")
# print_names()


# def user_info(**kwargs):
#     for info in kwargs.values():
#         print(info)
#
# user_info(name = "Juliana", age = 35, address = "Ramat Gan")
#
# def tasks_manager(*args):
#     if args:
#         for task in args:
#             print(f"today i need to do: {task}")
#     list = []
#     for task in args:
#         list.append(task)
#     print(f"Today i need to do: {' '.join(list)}")
#
#
# tasks_manager("task1", "task2")


def party_planner(*args, **kwargs):
    if args:
        print("You need to buy: ")
        for arg in args:
            print(arg)
    else:
        print("There is no food to buy")
    if kwargs:
        print("Party details: ")
        for key, value in kwargs.items():
            print(f"{key}:\n - {value}")
    else:
        print("No details about a party")


party_planner()
party_planner("1", "2", "3", place="Ramat Gan", owner="Juliana")
party_planner("1", "2", "3")
party_planner(place="Ramat Gan", owner="Juliana")

