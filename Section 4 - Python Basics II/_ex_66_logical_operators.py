is_magician = True
is_expert = False

# check if magician and expert: 'you are a master magician'
if is_magician and is_expert:
    print('you are a master magician')
# check magician but not expert 'at least you're getting there'
elif is_magician  :
    print('at least you\'re getting there')
# check not a magician: 'you need magic powers'
elif not is_magician:
    print('you need magic powers')