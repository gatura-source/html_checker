import dst
#Will be used in implementing a stack
import os
# for filesystem issues

import sys
# for system errors


tag_stack = dst.Stack()
##Stack used in the algorithm


##decorator function used to prime variables for the co_routines(send)


def prime(func):
    def inner(*args, **kwargs):
        v = func(*args, **kwargs)
        v.send(None)
        return v
    return inner



class html_tags_checker:
    ##initializing
    def __init__(self):
        """This method initializes the states where only three state
        of the FSM are needed, it also initializes the opening state and
         """
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.space = " "
        self.opening_tag_state = self._opening_tag()
        self.closing_tag_state = self._closing_tag()
        self.tag_keyword = self._tag_keyword()
        self.start = self._create_start()
        self.alpha_numeric = self.alphabet.upper() + "\"1234567890!@#$=_-|%^&*()/~" + self.space
        self.current_state = self.start
        self.stopped = False


    def send(self, char):
        """Sends current character to the next co_routine"""
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True


    def does_match(self):
        """this method at any point returns the state of the 
        string, does so by comparing current state with the closing_tag state sink_method"""

        if self.stopped:
            return False
        return self.current_state == self.closing_tag_state


    @prime
    def _create_start(self):
        """This method initializes the opening start as defined in
        FSM, it creates the state s"""

        while True:
            char = yield
            if char == '<':
                self.current_state = self.opening_tag_state
            else:
                break

    @prime
    def _opening_tag(self):
        """the method defines the opening tag state"""
        while True:
            char = yield
            if char in self.alpha_numeric or char in self.alphabet:
                self.current_state = self.tag_keyword
            elif char == '>':
                self.current_state = self.closing_tag_state
            else:
                break
    @prime
    def _tag_keyword(self):
        """Method defines the keyword of the HTML tag"""
        while True:
            char = yield
            if char in self.alpha_numeric or char in self.alphabet:
                self.current_state = self.tag_keyword
            elif char == '>':
                self.current_state = self.closing_tag_state
            else:
                break

    @prime
    def _closing_tag(self):
        """Method defines the closing tag state"""
        while True:
            char = yield
            if char in self.alpha_numeric or char in self.alphabet:
                self.current_state = self.tag_keyword
            elif char == '>':
                self.current_state = self.closing_tag_state
            else:
                break

def tags_check(word):
    """Producer Function"""
    checker = html_tags_checker()

    for char in word:
        checker.send(char)

    check_status = checker.does_match()
    return check_status


if __name__ == "__main__":

###Driver Code###
    def platform():
        if os.name == 'nt':
            slash = '\\'
        else:
            slash = '/'
        return slash
    acceptable_types = ["html", "htm"]

    unclosed_tags = []
    tags = ['area', 'base', 'br', 'col', 'command',
    'embed', 'hr', 'img', 'input', 'keygen', 'link',
    'meta', 'param', 'source', 'track', 'wbr']
    for _t in tags:
        unclosed_tags.append('<'+_t+'>')
        unclosed_tags.append('<'+_t.upper()+'>')
    base_dir = os.getcwd()
    f = input("Please enter the name of the HTML file:: ")
    f_name = base_dir + platform() + f
    try:
        with open(f_name, "r") as file:
            _fname, _ftype = f_name.split(".")
            if _ftype not in acceptable_types:
                print("File not allowed, check your filename and try again!!")
                sys.exit(-1)
            else:
                pass
            while True:
                try:
                    t = next(file)
                    status = tags_check(t.strip("\n"))
                    if status == True and t not in unclosed_tags:
                        if t[1] != '/':
                            tag_stack.push(t)
                        else:
                            try:
                                tag_stack.pop()
                            except IndexError:
                                pass



                except StopIteration:
                    break
        if tag_stack.is_empty():
            print("Your File is OK!!")
            sys.exit(0)
        else:
            print("Tags are not balanced!!")
            sys.exit(0)
    except FileNotFoundError:
        print("File not Found")
        sys.exit(-1)


