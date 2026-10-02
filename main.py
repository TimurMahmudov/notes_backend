import asyncio
from queries.notes_queries import notes_adding
from queries.users_queries import user_adding, user_get


print(asyncio.run(user_get(1)))


# async def main():
#    notes_data = {
#        "title": input("Input title: "),
#        "description": input("Input description: "),
#        "user_id": int(input("Input user_id: "))
#    }
#    result = await notes_adding(kwargs=notes_data)
#    print(result)
#    #    user_data = {
#    #        "username": input("Input username: "),
#    #        "password": input("Input password: "),
#    #    }
#    #    user_id = await user_adding(user_data)
#    #    return user_id
#
#
# if __name__ == "__main__":
#    asyncio.run(main())
