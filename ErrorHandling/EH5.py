
def poll(age):

    assert age>=18,"invalid"

    print("voted")

try:
    poll(14)

except Exception as e:

    print(e)
