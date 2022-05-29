let string = "http://youtube.com/watch?v=rj18UQjPpGA&feature=player_embedded";
string = "http://youtu.be/watajdsk"

let verifier = /http:\/\/(www\.)*youtube\.com\/.*/
let verifier2 = /https:\/\/(www\.)*youtube\.com\/.*/
let verifier3 = /http:\/\/youtube\.com\/.*/
let verifier4 = /https:\/\/youtube\.com\/.*/
let verifier5 = /http:\/\/youtu\.be\/.*/

let result = verifier.test(string)
if (result == false) {
   result = verifier2.test(string)
}
if (result == false) {
    result = verifier3.test(string)
}
if (result == false) {
    result = verifier4.test(string)
}
console.log(result);