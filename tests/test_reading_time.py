from lib.reading_time import *

def test_for_200_words():
    result = reading_time('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ultricies efficitur ullamcorper. Proin urna urna, efficitur bibendum pharetra ut, condimentum eget ligula. Duis sit amet dignissim nisl, a pharetra nisi. Phasellus laoreet sollicitudin nunc sodales mollis. Fusce at blandit metus. Sed et aliquam elit, eu varius dolor. In ultrices ultricies libero, eu ullamcorper tellus mollis vitae. Curabitur facilisis lorem eu nibh ornare, ut eleifend massa interdum. Maecenas sagittis diam non nisl ornare dictum. Nam ut sem ac orci venenatis fermentum nec eget risus. Suspendisse aliquam sem tellus, quis bibendum ante vehicula id. Phasellus posuere facilisis augue nec molestie. Proin blandit accumsan libero, a interdum ipsum porta nec. Proin vestibulum lectus quam, quis commodo ex sodales sit amet. Donec congue turpis eget faucibus venenatis. Ut elementum ante ut pharetra pharetra. In lacinia laoreet ipsum, at accumsan erat sagittis tincidunt. Nunc ultrices est vel tempor ultrices. Suspendisse a ligula convallis, malesuada dui vel, ullamcorper metus. Aliquam erat volutpat. Nam erat mauris, molestie sed ultricies ut, gravida euismod lorem. Nulla at facilisis arcu. Nulla convallis, nisl eget rutrum maximus, libero nunc aliquet tellus, id dapibus ipsum lacus ut odio. Morbi sagittis ultrices nisi, dignissim sodales massa scelerisque in. Fusce quis lorem ut mauris.')
    assert result == 1.0


"""
given 200 words
reading_time('200') 
==> 1.0

given 400 words 
reading_time('400') 
==> 2.0

given 300 words 
reading_time('600') 
==> 1.5

given 700 words
reading_time('700')
==> 3.5

given 0 words 
reading_time('')
==> 'No text added!'
"""
