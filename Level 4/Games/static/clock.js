var timer = undefined;
var duration = undefined;
var pausedTime = 0;

function startClock(pausedTime) {
    var start = new Date().valueOf() - 1000 * pausedTime;
    var clock = setInterval(function() {        
        var now = new Date().valueOf();
        duration = Math.round((now - start)/1000);
        var minutes = Math.floor(duration/60)
        var seconds = duration % 60;
        seconds = seconds < 10 ? "0" + seconds : seconds
        message = minutes + ":" + seconds;
        $("#clock").text(message);
    }, 1000);
    return clock;
}

function stopClock() {
    clearInterval(timer);
    timer = undefined;
    matches = 0;
    pausedTime = 0;
}

function pauseClock() {
    pausedTime = duration;
    clearInterval(timer);
    timer = undefined;    
}

