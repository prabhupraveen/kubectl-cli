from cmd import Cmd
import subprocess
import os
 
class MyPrompt(Cmd):
    
    intro = "Welcome! Type ? to list commands"
    kubectlcmd = ['kubectl']
    namespace = "default"
    clearcmd = ""

    def __init__(self):
        super(MyPrompt, self).__init__()
        self.set_prompt(self.get_cur_context(), self.namespace)
        if os.name == "posix":
            self.clearcmd = "clear"
        else:
            self.clearcmd = "cls"

    def do_set_context(self, inp):
        self.process_cmd("config use-context {}".format(inp))
        self.set_prompt(self.get_cur_context(), self.namespace)
    
    def do_get_contexts(self, inp):
        self.process_cmd("config get-contexts")

    def do_set_namespace(self, inp):
        inp = inp.strip()
        if len(inp.split()) > 1:
            print("ERROR: namepsace cannot have spaces")
        else:
            self.namespace = inp
            self.set_prompt(self.get_cur_context(), self.namespace)

    def do_clear(self, inp):
        os.system(self.clearcmd)

    def do_khelp(self, inp):
        result = subprocess.run(self.kubectlcmd, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        print("{}\n".format(result))
    
    def help_set_context(self):
        print("Set the current kubernetes context\n")

    def help_get_contexts(self):
        print("List the kubernetes contexts\n")

    def help_set_namespace(self):
        print("Set the kubernetes namespace\n")

    def help_clear(self):
        print("Clear the screen\n")

    def help_exit(self):
        print("exit the application. Shorthand: x q Ctrl-D.")
    
    def help_khelp(self):
        print("Print kubectl help")

    def do_exit(self, inp):
        print("Bye")
        return True
    
    def set_prompt(self, ctx, ns=None):
        if ns == None:
            self.prompt = "{}> ".format(ctx)
        else:
            self.prompt = "{}@{}> ".format(ns, ctx)

    def get_cur_context(self):
        return subprocess.run(['kubectl', 'config', 'current-context'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

    def process_cmd(self, inp):
        args = inp.split()
        finalCommand = self.kubectlcmd + args
        if inp.find('-A') < 0 and args[0] != "config":
            finalCommand = finalCommand + ['-n', self.namespace]
        result = subprocess.run(finalCommand, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        print("{}\n".format(result))
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        else:
            if inp.find("use-context") > 0:
                cmds = inp.strip().split()
                if len(cmds) == 3:
                    self.do_set_context(cmds[2])
                else:
                    print("To set context use command set_context <context>")
            else:
                return self.process_cmd(inp)
 
    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()