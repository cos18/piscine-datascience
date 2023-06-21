from time import time, localtime, strftime

# https://docs.python.org/ko/3/library/time.html
sec = time()
print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation".format(sec))
print(strftime("%b %d %Y", localtime()))