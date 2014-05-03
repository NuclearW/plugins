import hexchat

__module_name__ = 'MyMessages-prefix'
__module_author__ = 'TingPing'
__module_version__ = '1'
__module_description__ = 'Properly show your messages in ZNC with the privmsg-prefix module'

def privmsg_cb(word, word_eol, userdata, attrs):
	mynick = hexchat.get_info('nick')
	sender = word[0].split('!')[0][1:]
	sendfrom = word[0].split('!')[1][0:]
	network = hexchat.get_info('network')
	msg = word_eol[3][1:]

	if hexchat.nickcmp(sendfrom, 'prefix@privmsg.znc.in') == 0:
		hexchat.command('query -nofocus {}'.format(sender))

		if '\001ACTION' in msg:
			for repl in ('\001ACTION', '\001'):
				msg = msg.replace(repl, '')

			msg = msg[3:]
			hexchat.find_context(network, sender).emit_print('Your Action', mynick, msg.strip(), time=attrs.time)
		else:
			msg = msg[3:]
			hexchat.find_context(network, sender).emit_print('Your Message', mynick, msg, time=attrs.time)

		return hexchat.EAT_ALL

hexchat.hook_server_attrs('PRIVMSG', privmsg_cb)
