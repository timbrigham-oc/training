from app.utility.base_world import BaseWorld

name = 'GameBoard plugin'
challenge = 'Run a red-blue exercise'


async def verify(services):
    for r in  await services.get('data_svc').locate('operations', dict(access=BaseWorld.Access.RED)):
        for b in await services.get('data_svc').locate('operations', dict(access=BaseWorld.Access.BLUE)):
            if r.start < b.finish:
                return True
    return False
