import os
import sys	

print("\nPages to explore")
print("----------------")
print("ilab - Check status of Virtual Computers")
print("valgrind - Check info on valgrind tool")
print("syslab - System_programing first lab")
print("in-band - Difference between in-band and out-of-band")
print("recurrence - Recurrence Relations")
print("asymptotic - Review of Algorithm")
print("xterm - Terminal Control Sequences")
print("insert-sort[-i] - Insertion sort")
print("quick-sort[-q] - Quick sort using c")
print("manual - System programming manual")
print("engineer - System reverse engineer book")
print("assembly - Information on assembly language")
print("ddd - DataDisplayDebugger")
print("gitlib - git:librarysource")
print("c-pro - Programming and UNIX")
print("c-quo - C-Programming interview questions")
print("signals - GNU library for signal handlers")
print("heroku - Heroku Dev Center")
print("portal - google portal home")
print("postgres - Heroku Postgres")
print("ocamal - Learning OCamal")
print("scheme - Learning scheme function are essential")
print("---------------")
print("\n")

user = input("Are you sure(yes/no): ")
if user == "no":
	print("Goodbye")
	exit(0)

def dispatch_web_pages(www):
	return{
		'ilab': lambda: os.system("open https://report.cs.rutgers.edu/nagiosnotes/ilab-machines.html"),
		'valgrind': lambda: os.system("open http://cs.ecs.baylor.edu/~donahoo/tools/valgrind/"),
		'syslab': lambda: os.system("open https://content.sakai.rutgers.edu/access/content/attachment/c2bbfa03-c6d8-4246-be54-f1025caec594/Assignments/d3587e68-e06c-4d9e-85ff-6eab64018c02/Asst0.txt"),
		'in-band': lambda: os.system("open https://www.quora.com/What-are-the-differences-between-in-band-and-out-band-management"),
		'asymptotic': lambda: os.system("open https://vimeo.com/388890476"),
		'recurrence': lambda: os.system("open https://vimeo.com/390367591"),
		'xterm': lambda: os.system("open https://invisible-island.net/xterm/ctlseqs/ctlseqs.html"),
		'-i': lambda: os.system("open https://www.youtube.com/watch?v=ep8uG1IBApQ"),
		'-q': lambda: os.system("open https://hackr.io/blog/quick-sort-in-c"),
		'manual': lambda: os.system("open http://man7.org/linux/man-pages/man3/fopen.3.html"),
		'engineer': lambda: os.system("open https://torus.company/writings/RE4B-EN.pdf"),
		'assembly': lambda: os.system("open https://hackr.io/tutorials/learn-assembly-language"),
		'ddd': lambda: os.system("open https://www.gnu.org/software/ddd/"),
		'gitlib': lambda: os.system("open https://sourceware.org/git/"),
		'c-pro': lambda: os.system("open http://www.cs.miami.edu/home/schulz/CSC322.pdf"),
		'c-quo': lambda: os.system("open https://fresh2refresh.com/c-programming/c-interview-questions-answers/"),
		'sig': lambda: os.system("open https://www.gnu.org/software/libc/manual/html_node/Signal-Handling.html"),
		'heroku': lambda: os.system("open https://devcenter.heroku.com/articles/heroku-cli-autocomplete"),
		'portal': lambda: os.system("open https://admin.google.com/u/2/ac/home"),
		'postgres': lambda: os.system("open https://devcenter.heroku.com/articles/heroku-postgresql#local-setup"),
		'ocamal': lambda: os.system("open https://baturin.org/docs/ocaml-faq/#the-double-semicolon"),
		'scheme': lambda: os.system("open https://docs.racket-lang.org/reference/pairs.html"),
	}.get(www, lambda: None)()

if user == "yes":
	www = input("Enter website: ")
	dispatch_web_pages(www)


