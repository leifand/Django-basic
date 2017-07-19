import string
import random
from django.shortcuts import render

# a decent random word gen I found on Stack Overflow
def random_word():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))

def index(request):
    # setup session counter - Django stores session on server!
    if 'word_count' in request.session:
        request.session['word_count'] = request.session['word_count'] + 1
    else:
        request.session['word_count'] = 0;
    count = request.session['word_count']
    # gen word
    word = random_word()
    data = {
        'word_count' : count,
        'random_word' : word
    }

    return render(request, 'randomword/index.html', data)
