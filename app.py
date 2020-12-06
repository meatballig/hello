#!/usr/bin/env python3

import datetime

def do_magic():
  now = datetime.datetime.now()
  return "Hello! {0}".format(now)

if __name__ == "__name__":
  print(do_magic())

print(datetime.datetime.now())
