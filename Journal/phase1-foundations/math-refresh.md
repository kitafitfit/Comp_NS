Bayesian: 

gmail ve spam mailler ornegim soyleydi: 

2% of my emails are spam and gmail is 96% of the time succesfull on tagging the spam emails. 
On the other hand, google wrongly tags spams some of my important emails, like 1% of the time. 

just to add some more complexity into the game; 5% of spam emails are phishing and if I happen to click them, I get scammed. 

Given an email is not tagged as spam, what is the probability that it will be a phishing email and cause damage to the user?

Cozumun ilk asamasi:
Ornek olarak 10000 tane email geldigini dusunelim. 

when 96 % of the SPAM emails are correctly tagged, means 4% are not tagged but actually spam. (so they are in my important folder) right?  
when 1% of emails are actually not spam but tagged as spam incorrectly means 99% of them are important and not tagged as spam (so they are also in my important folder)
Bu durumda inboxta toplam 9710 email var. Spam olarak taglenmemis emailler bunlar. 

%2 si spam olduguna gore 10000* 2% = 200 tane spam ve 9800 tane spam olmayan enail var genel olarak. (Prior) 

P (H|E) = (200 * 0.04) / (200*0.04) + (9800*0.99) = 8 / 9710 = 0.0008  this is the probability of a spam email that is not tagged as spam. (posterior) yanei 8 tane email. 


Simdi ikinci asamaya gelirsek:
5% phishing olasiligi var. 
8* .05  = 0.4 tane email phishing yapiyor. 
inboxta toplam 9710 tane email oldugu icin de probability (ratio) = 0.4 / 9710 = 0.00004 oluyor.  
