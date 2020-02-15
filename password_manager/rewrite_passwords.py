# A simple tool to convert from human readable format to the script accepted format and back
# Does NOT permit colons in password descriptor

rewrite = input('Rewrite to script accepted format (option "a") or write to human-readable format (option "b")?\n')
if rewrite.lower() == 'a':
	f = open('passwords_formatted.txt', 'r')
	p_list = []
	passwords = []
	for line in f:
		split_line = line.split(':', 1)
		p_list += [split_line[0]]
		passwords += [split_line[1]]
	f.close()
	f = open('passwords.txt', 'w')
	f.write(str(p_list) + '\n')
	for password in passwords:
		f.write(password.strip() + '\n')
	f.close()
if rewrite.lower() == 'b':
	f = open('passwords.txt', 'r')
	p_list = eval(f.readline())
	passwords = []
	for p in p_list:
		passwords += [f.readline().strip()]
	f.close()
	f = open('passwords_formatted.txt', 'w')
	for idx in range(len(p_list)):
		f.write(p_list[idx] + ': ' + passwords[idx] + '\n')
	f.close()
