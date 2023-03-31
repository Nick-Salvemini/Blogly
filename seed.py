from models import User, Post, Tag, PostTag, db
from app import app

db.drop_all()
db.create_all()

# USERS ------------------------------------------------------------

u1 = User(first_name='Jean Paul', 
        last_name='Jean Paul', 
        image_url='https://images.unsplash.com/photo-1615813967515-e1838c1c5116?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')
u2 = User(first_name='Wendy', 
        last_name='Bendy', 
        image_url='https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')
u3 = User(first_name='Michelle', 
        last_name='Bichelle', 
        image_url='https://images.unsplash.com/photo-1542596768-5d1d21f1cf98?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')
u4 = User(first_name='Notta', 
        last_name='Cat', 
        image_url='https://images.unsplash.com/photo-1503777119540-ce54b422baff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=772&q=80')
u5 = User(first_name='Bandit', 
        last_name='Heeler', 
        image_url='https://images.unsplash.com/photo-1529956226996-84082d2a23ab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1287&q=80')

db.session.add_all([u1,u2,u3,u4,u5])
db.session.commit()

# TAGS ------------------------------------------------------------

t1 = Tag(name='Funny')
t2 = Tag(name='Games')
t3 = Tag(name='Random')
t4 = Tag(name='Cooking')
t5 = Tag(name='Help!')
t6 = Tag(name='Coding')
t7 = Tag(name='ELI5')
t8 = Tag(name='Sports')

db.session.add_all([t1,t2,t3,t4,t5,t6,t7,t8])
db.session.commit()

# POSTS ------------------------------------------------------------

p1 = Post(title='I accidentally sneezed during an auction & now I own the entire Artic Circle.', 
        user_id=u1.id, 
        tags_for_post=[PostTag(tag_id=t3.id), 
                       PostTag(tag_id=t1.id)])
p2 = Post(title='Have you ever noticed? Some people are dentists and some arent', 
        content='You never meet someone who is just a bit of a dentist', 
        user_id=u2.id, 
        tags_for_post=[PostTag(tag_id=t3.id)])
p3 = Post(title='Instacart gave me 50 lbs of limes instead of 5 lbs. what the hell do I do with 50 pounds of limes?', 
        content='Ive already donated a bunch and gave a bunch away. Im planning on making a bunch of lime-themed cocktails, but... jeez. Ceviche?', 
        user_id=u3.id, 
        tags_for_post=[PostTag(tag_id=t4.id)])
p4 = Post(title='how to clean dogs pee from wall', 
        content='My dog peed on the wall a few hours ago and its already dry but I dont know how to get rid of the stain :/ any tips on how to do that?', 
        user_id=u4.id, 
        tags_for_post=[PostTag(tag_id=t5.id)])
p5 = Post(title='I feigned colorblindness to avoid workplace uniform requirements', 
        content='I worked as a valet and they had strict uniform requirements, including black pants. Mine were dark Grey. I knew all along I was committing an infraction, but refused to spend money on more pants just for a part time job. Four months into the job they noticed and called me out but I maintained they were black. A debate arose, then someone asked cautiously if I was colorblind. I said "well if youre so sure Im wrong about this then I may be, its been suggested before". I dont even think thats how colorblindness works. Nevertheless, the management took pity on me. I never corrected the error, nor was i disciplined. I share this to atone for my sins.', 
        user_id=u5.id, 
        tags_for_post=[PostTag(tag_id=t5.id),
                       PostTag(tag_id=t3.id)])
p6 = Post(title='Question about respawning.', 
        content='Hello, quick question about if it is explained in the game about the character not being able to respawn. I will elaborate, when in a party, a party member is defeated, you can still keep playing and if you win the battle they will respawn, saying something about it. But if Lea dies the game does a rollback in time like it didnt happend even if your party was gonna win the battle. Even Fake Lukas can do it so is not like the cause is being a avatar. So is there a explanation about it somewhere? Anyone knows?', 
        user_id=u2.id, 
        tags_for_post=[PostTag(tag_id=t2.id)])
p7 = Post(title='ELI5: how do architects calculate if a structure like a bridge is stable?', 
        user_id=u4.id, 
        tags_for_post=[PostTag(tag_id=t7.id)])
p8 = Post(title='Little Johnnys parents wanted to have some "alone time" together...', 
        content='... so they sent Johnny out onto the porch with an ice-cream sandwich. Not wanting the boy to finish too quickly, his mother came up with an idea to keep him distracted. "While youre eating that," she said, "watch the neighborhood and tell us everything interesting that you see." A few minutes in to their lovemaking, Johnnys parents heard him yell his first report: "The Hendersons got a new car!" "Thats great!" answered his mother. "Keep looking!" More time passed, and Johnny shouted again: "The Smiths are planting flowers!" "Good job!" responded his father. "Keep looking!" Another minute went by, and Johnny called out for a third time: "Mister and Missus Johnson are having sex!" Johnnys parents abruptly stopped in their own activity. After a moment of silence, his mother replied with "How do you know that theyre having sex, Johnny?" "Because Billy Johnson is eating an ice-cream sandwich on their porch!"', 
        user_id=u2.id, 
        tags_for_post=[PostTag(tag_id=t1.id)])
p9 = Post(title='Just bought my first sous vide, other than steaks what else should I use it for ?', 
        user_id=u5.id, 
        tags_for_post=[PostTag(tag_id=t4.id)])
p10 = Post(title='Learn python for a 13 year old', 
        content='Hi, as the title stated, I am 13 years old and want to learn python. I have a good amount of knowledge and experience with basic python up until classes. However,I am now stuck as it is getting to complicated to understand. I have tried 30 days of python on github and automate the boring stuff but as I stated were too complicated for me to understand. Python and coding is just a hobby as I want to learn some fundamentals before delving into harder programming languages like java script or c++. Preferably, I would like the course/roadmap/resource to be free and for me 2 just scrolls and read/watch for about 30 minutes a day. Thank you for reading this and have a nice day:)', 
        user_id=u1.id, 
        tags_for_post=[PostTag(tag_id=t6.id)])

db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
db.session.commit()

