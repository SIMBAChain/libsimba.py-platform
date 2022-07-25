from test_contract_vt3 import Test_contract_vt3
import asyncio
import requests

tcv3 = Test_contract_vt3()
# res = tcv3.setNum_sync(_ourNum=88)
# print(f'sync res: ${res}\n\n')

# get_res_sync = tcv3.getNum_sync()
# print(f'get_res_sync: {get_res_sync}\n\n')

# query_res = tcv3.setNum_sync(do_query=True)
# print(f'query_res: {query_res}\n\n')
# async def main():
#     get_res = await tcv3.getNum()
#     print(f'get_res: ${get_res}')

# asyncio.run(main())

file_name = 'test_file'
file_path = './test_file.jpg'
file_name_2 = 'test_file_2'
file_path_2 = 'test_file_2.jpg'
files = [(file_name, file_path, 'rb')]

name = "Charlie"
age = 99
street = "rogers street"
number = 123
town = "new york"
addr = tcv3.Addr(street, number, town)
p = tcv3.Person(name, age, addr)
async def main():
    file_res = await tcv3.structTest5(p, files)
    print(f'file_res: {file_res}')

asyncio.run(main())

# file_res = tcv3.structTest5_sync(p, files)
# print(f'file_res: {file_res}')
    