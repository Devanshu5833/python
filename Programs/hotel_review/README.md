Write a Python program which can gives the feedback overview with mentioned words for hotels.

There are statements/feedbacks given by customers available in file. 

Enter a comma seperated target mentions:
breakfast location staff fun happy city center food good service


feedback.txt
------------------------
1  # <- this is hotel ID
I came from south india, the location of hotel was too good, I'm happy with the city location and food. 6
2
We recently visited this hotel, the staff was awesome and service and ofcourse the breakfast, it was amazing. We are haapy with this hotel.
...
...
<Consider attached feedback.txt>


Output in Json:
{
"mentions": {
"breakfast": 5,
"food": 2,
"happy":2,
...

}
"topStatement": { 
# highest number of applicable mentions.
"desc": "I came from south india, the location of hotel was too good, I'm happy with the city location and food.",
"hotelid": 1
}
"hotels": [1,2,4,5] # hotel sorted by number of mentions - desc order
}
