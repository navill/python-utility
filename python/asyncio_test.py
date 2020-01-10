import asyncio
import random

"""
목적에 따라 아래의 두 함수를 선택해 결과 출력
 - run_until_complete: 실행 완료에 상관없이 실행된 순서로 결과값을 가져온다.
 - ensure_future: 실행이 완료된 순서로 결과값을 가져온다. 
"""


async def network_request(number):
    integer = random.randint(1, 3)
    await asyncio.sleep(integer)  # sleep 시간만큼 통신이 이루어진다고 가정
    return {"success": True, "result": number ** 2}


async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))


loop = asyncio.get_event_loop()
# 순서대로 실행 결과 출력
loop.run_until_complete(fetch_square(2))
loop.run_until_complete(fetch_square(3))
loop.run_until_complete(fetch_square(4))

# # 연산이 완료되는대로 실행결과 출력
# asyncio.ensure_future(fetch_square(2))
# asyncio.ensure_future(fetch_square(3))
# asyncio.ensure_future(fetch_square(4))
# loop.run_forever()
