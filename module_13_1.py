import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        p
        print(f"Силач {name} поднял {i} шар")
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Олег', 2))
    task2 = asyncio.create_task(start_strongman('Мустанг', 5))
    task3 = asyncio.create_task(start_strongman('Машина', 1))
    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(start_tournament())
