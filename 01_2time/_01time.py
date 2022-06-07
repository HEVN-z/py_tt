from iqoptionapi.stable_api import IQ_Option
import time
bot = IQ_Option('dummy.esper@gmail.com', '12651265exe')
bot.connect()
server_time = bot.get_server_timestamp()
final_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.ctime(server_time))
print(final_time)