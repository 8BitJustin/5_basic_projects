# Mad Libs Generator project

def mad_libs():

	name = input("Can I have your name please? ")
	noun = input("Please provide a noun: ")
	adjective = input("Please provide an adjective: ")
	verb = input("Please provide a verb: ")

	message = f"Hello, I'm {name}. I'm a {noun}, a very {adjective} {noun}" \
		f" and I love to {verb}."

	print(message)


mad_libs()
