#!/usr/bin/python3
./6_new_str_print..py
variable = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."
variable = variable.replace("and preferably only one", "preferably only one way unless ")
print(variable)

variable = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."
variable = variable.replace(variable, "preferably only one way unless ")
print(variable)
