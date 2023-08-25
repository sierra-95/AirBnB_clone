#!/usr/bin/python3
'''
HBNBCommand - console for the airbnb clone
'''

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import os.path
import json
import shlex


class HBNBCommand(cmd.Cmd):
    '''HBNBCommand - console for the airbnb clone'''
    prompt = '(hbnb) '
    __file_path = 'file.json'
    model_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, inp):
        '''do_quit - Quit command to exit the program'''
        return True

    def emptyline(self):
        '''emptyline - do nothing'''
        pass

    def do_EOF(self, inp):
        '''do_EOF - Quit command to exit the program'''
        return True

    def do_create(self, inp):
        '''do_create - create a new instance of a model'''
        model_list = ['BaseModel', 'User', 'State',
                      'City', 'Amenity', 'Place', 'Review']
        if len(inp) == 0:
            print("** class name missing **")
        elif inp in self.model_list:
            new = eval(inp)()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, inp):
        '''do_show - show prints the string representation of an instance'''
        if len(inp) == 0:
            print("** class name missing **")
        else:
            a_list = inp.split()
            if a_list[0] not in self.model_list:
                print("** class doesn't exist **")
            elif len(a_list) == 1:
                print("** instance id missing **")
            elif a_list[0] in self.model_list and len(a_list) == 2:
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path,
                              encoding='utf-8', mode='r') as f:
                        a_string = f.read()
                        if a_string:
                            a_dict = json.loads(a_string)
                            a_list[1] = a_list[1].replace("'", "")
                            a_list[1] = a_list[1].replace("\"", "")
                            if a_list[0] + '.' + a_list[1] in a_dict:
                                print(eval(a_list[0])
                                      (**(a_dict[a_list[0] +
                                                 '.' + a_list[1]])))
                            else:
                                print("** no instance found **")
                        else:
                            print("** no instance found **")
                else:
                    print("** no instance found **")

    def do_destroy(self, inp):
        '''do_destroy - destroy an instance'''
        if len(inp) == 0:
            print("** class name missing **")
        else:
            a_list = inp.split()
            if a_list[0] not in self.model_list:
                print("** class doesn't exist **")
            elif len(a_list) == 1:
                print("** instance id missing **")
            elif a_list[0] in self.model_list and len(a_list) == 2:
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path,
                              encoding='utf-8', mode='r') as f:
                        a_string = f.read()
                        a_dict = json.loads(a_string)
                        a_list[1] = a_list[1].replace("'", "")
                        a_list[1] = a_list[1].replace("\"", "")
                        if a_list[0] + '.' + a_list[1] in a_dict:
                            del a_dict[a_list[0] + '.' + a_list[1]]
                        else:
                            print("** no instance found **")
                    with open(self.__file_path,
                              encoding='utf-8', mode='w') as f:
                        f.write(json.dumps(a_dict))
                else:
                    print("** no instance found **")

    def do_all(self, inp):
        '''do_all - show all instances of a class or all'''
        flag = 0
        flag2 = 0
        if len(inp) == 0:
            flag = 1
            flag2 = 1
        if len(inp) > 0:
            a_list = inp.split()
            if a_list[0] in self.model_list and len(a_list) == 1:
                flag = 1
            else:
                print("** class doesn't exist **")
                flag = 0
        if flag == 1:
            if flag2 == 0:
                eval_class = eval(a_list[0])
            instances = []
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, encoding='utf-8', mode='r') as f:
                    a_string = f.read()
                    if a_string:
                        a_dict = json.loads(a_string)
                        for key, value in a_dict.items():
                            if flag2 == 0:
                                if a_list[0] in key:
                                    instances.append(eval_class.__str__
                                                     (eval_class(**(value))))
                            if flag2 == 1:
                                eval_class2 = eval(value['__class__'])
                                instances.append(eval_class2.__str__
                                                 (eval_class2(**(value))))
                        print(instances)
            else:
                list_vacia = []
                print(list_vacia)

    def do_update(self, inp):
        '''do_update - update an instance'''
        if len(inp) == 0:
            print("** class name missing **")
        else:
            a_list = shlex.split(inp)
            if a_list[0] not in self.model_list:
                print("** class doesn't exist **")
            elif len(a_list) == 1:
                print("** instance id missing **")
            elif len(a_list) == 2:
                print("** attribute name missing **")
            elif len(a_list) == 3:
                print("** value missing **")
            elif a_list[0] in self.model_list and len(a_list) >= 4:
                a_list[3] = a_list[3].replace("'", "")
                a_list[3] = a_list[3].replace("\"", "")
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path,
                              encoding='utf-8', mode='r') as f:
                        a_string = f.read()
                        a_dict = json.loads(a_string)
                        if a_list[0] + '.' + a_list[1] in a_dict:
                            a_dict[a_list[0] + '.' +
                                   a_list[1]][a_list[2]] = a_list[3]
                            dict1 = a_dict[a_list[0] + '.' + a_list[1]]
                            new_instance = eval(a_list[0])(**dict1)
                            new_instance.save()
                        else:
                            print("** no instance found **")
                else:
                    print("** no instance found **")

    def do_count(self, inp):
        '''do_count - return the number of instances'''
        if len(inp) > 0:
            a_list = inp.split()
            if a_list[0] in self.model_list and len(a_list) == 1:
                count = 0
                if os.path.isfile(self.__file_path):
                    with open(self.__file_path, encoding='utf-8',
                              mode='r') as f:
                        a_string = f.read()
                        if a_string:
                            a_dict = json.loads(a_string)
                            for key, value in a_dict.items():
                                if a_list[0] in key:
                                    count += 1
                print(count)

    def default(self, inp):
        '''default - process other type of input'''
        tokens = inp.split('.')
        if tokens is not None and len(tokens) > 1:
            method = tokens[1].split('(')
            if method is not None:
                arguments = method[1].split(',')
                if arguments is not None:
                    for i in range(len(arguments)):
                        arguments[i] = arguments[i].replace("'", "")
                        arguments[i] = arguments[i].replace(")", "")
                        final_list = [tokens[0]] + arguments
                        str_final = ' '.join(str(e) for e in final_list)
                        str_final = str_final.replace(")", "")
                        if method[0] == 'all' and len(arguments) == 1:
                            return(self.do_all(str_final))
                        elif method[0] == 'show' and len(arguments) == 1:
                            return(self.do_show(str_final))
                        elif method[0] == 'destroy' and len(arguments) == 1:
                            return(self.do_destroy(str_final))
                        elif method[0] == 'update':
                            if "{" in inp:
                                update_list = [tokens[0]]
                                str_bef_dict = inp.split(',', 1)[-1]
                                str_bef_dict = str_bef_dict.replace(")", "")
                                str_bef_dict = str_bef_dict.replace("'", "\"")
                                dict1 = eval(str_bef_dict)
                                if type(dict1) is dict:
                                    for key, value in dict1.items():
                                        update_list = [tokens[0]]
                                        update_list.append(arguments[0])
                                        update_list.append(key)
                                        update_list.append(value)
                                        str_update = ' '.join(
                                            str(e) for e in update_list)
                                        self.do_update(str_update)
                                return
                            else:
                                return(self.do_update(str_final))
                        elif method[0] == 'count' and len(arguments) == 1:
                            return(self.do_count(str_final))
                        else:
                            return(cmd.Cmd.default(self, inp))
        return(cmd.Cmd.default(self, inp))

if __name__ == '__main__':
    '''main'''
    HBNBCommand().cmdloop()
