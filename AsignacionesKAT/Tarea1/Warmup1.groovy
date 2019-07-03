/*The parameter weekday is true if it is a weekday, and the parameter vacation
is true if we are on vacation. We sleep in if it is not a weekday or we're on
vacation. Return true if we sleep in.

sleepIn(false, false) → true
sleepIn(true, false) → false
sleepIn(false, true) → true
*/

def sleepIn(boolean weekday, boolean vacation) {

boolean reSleepIn = false;
if (!weekday || vacation){
  reSleepIn = true;
}
return reSleepIn;
}


w = new Warmup1()
println(w.sleepIn(false, false))
println(w.sleepIn(true, false))
println(w.sleepIn(true, false))
