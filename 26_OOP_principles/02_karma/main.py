import logging, random


class KillError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class DrunkError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CarCrashError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class GluttonyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class DepressionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def one_day():
    try:
        karma = random.choices(
            [
                random.randint(1, 7),
                random.choice(
                    [
                        KillError('Murder'), DrunkError('Got Drunk'),
                        CarCrashError('Car crashed'), GluttonyError('Eaten too much'),
                        DepressionError('Fallen into depression')
                    ]
                )
            ], weights=[9, 1]
        )

        if isinstance(karma[0], int):
            return karma[0]
        else:
            raise karma[0]

    except KillError:
        log.error(KillError('Murder'))
        return -1
    except DrunkError:
        log.error(DrunkError('Drunk'))
        return -1
    except CarCrashError:
        log.error(CarCrashError('Car Crashed'))
        return -1
    except GluttonyError:
        log.error(GluttonyError('Eaten too much'))
        return -1
    except DepressionError:
        log.error(DepressionError('Fallen into depression'))
        return -1


your_karma = 0
logging.basicConfig(filename='karma.log', level=logging.ERROR)
log = logging.getLogger('karma')

while your_karma < 500:
    your_karma += one_day()
    print(your_karma)
else:
    print('Your karma raised to the top points - 500')
