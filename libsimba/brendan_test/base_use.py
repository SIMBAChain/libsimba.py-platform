from libsimba.simba import Simba

simba = Simba()


import asyncio


# Using Simba and async/await
class Example:
    async def do_something(self):
        apps = await simba.list_applications()
        # .. do something with apps

# Making a call and viewing printed result:
async def main():
    apps = await simba.list_applications()
    print(f'apps from async call:\n\n{apps}\n\n')
asyncio.run(main())


from libsimba.simba import SimbaSync
simba_sync = SimbaSync()

# Using SimbaSync with synchronous behavior
class SyncExample:
    async def do_something(self):
        apps = simba_sync.list_applications()
        # .. do something with apps

# Making a call and viewing printed result:
def main():
    apps = simba_sync.list_applications()
    print(f'apps from sync call:\n\n{apps}\n\n')
main()



from libsimba import SearchFilter

async def main():
    apps = await simba.list_applications(
        search_filter=SearchFilter(name__exact='a123')
        )
    print(f'async results with SearchFilter:\n\n{apps}\n\n')
asyncio.run(main())

contracts = simba_sync.list_contracts("BrendanTest")
print(f'contracts: {contracts}\n\n')

contract_info = simba_sync.list_contract_info("BrendanTestApp", "test_contract_vt3")

