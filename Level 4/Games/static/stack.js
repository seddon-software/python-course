class Stack {

    transfer(fromStack, cards, undo, type) {
        function isUp() {  // array is stored backwards, e.g. [31 56 3] -> [5 4 3] after extracting pips
            return pip(cards[0]) - pip(cards[cards.length-1]) > 0;
        }
        
        var toStack = this;

        // journal transfer
        if(!undo) addToJournal(type, cards.slice(), fromStack, toStack);

        var count = cards.length;
        for(var i = 0; i < count; i++) {
            fromStack.cards.pop();
        }
        
        if(toStack.type === "bank" && undo === false)
            cards = cards.reverse(); 
        else if(isUp() && undo === false) 
            cards = cards.reverse();
        
        for(var i = 0; i < count; i++) {
            var card = cards.pop();
            toStack.cards.push(card);
            var div = DOM[card];
            div.data("card-info").stackIndex = toStack.index;
        }
      
        fromStack.resetDragAndDrop();
        toStack.resetDragAndDrop();

        // make sure top card is visible
        var top;
        if(type === "table") top = fromStack.getTop();
        if(type === "deal") top = toStack.getTop();
        if(cardIsFaceDown(top)) {
            addToJournal("flip", [top], fromStack, toStack, undo);           
            flip(top);
        }

        redraw();
    }
    
    static howManyEmptyStacks() {
        var count = 0;
        for(var i = 0; i < stacks.length; i++) {
            var stack = stacks[i];
            if(stack.type === "table" && stack.length() === 0) count++;
        }
        return count;            
    }
    
    stackWillAccept(dragStack) {
        // examples:
        //
        // a) dropStack = [x x x 8], dropTop = 8
        //    dragStack = [x x x 5 6 7], up = [7 6 5], sequence = 2
        //    transfer whole "up" stack if(dropTop - up[0] == 1)
        //
        // b) dropStack = [x x x J], dropTop = 11
        //    dragStack = [x x 10 9 8 7 6 5], down = [5 6 7 8 9 10], sequence = -5
        //    if 0 free stacks, 1 card  can be transferred, so transfer nothing
        //    if 1 free stacks, 2 cards can be transferred, so transfer nothing
        //    if 2 free stacks, 4 cards can be transferred, so transfer part of "down" stack: [7 8 9 10]
        //    if 3 free stacks, 8 cards can be transferred, so transfer all of "down" stack: [5 6 7 8 9 10]
        //
        
        function getSequence() {
            if(up.length > down.length) 
                return pip(up[0]) - pip(up[up.length-1]);  // up returns >= 0
            else
                return pip(down[0]) - pip(down[down.length-1]); // down returns <= 0 
        }

        function promptForCards(result) {
            // this function is called:
            //  a) for all up sequences
            //  b) for down sequences when
            //        1. moving to an empty stack
            //        2. moving to a bank stack
            function getCSS() {
                var css = {};
                css["position"] = "absolute";
                css["width"] = `${WIDTH}vw`;
                css["left"] = `${(WIDTH+1)*i}vw`;
                css["bottom"] = `${k*2}vh`;
                css["z-index"] = `${1000-k}`;
                return css;
            }
            var cardWidth = $(window).width() * WIDTH / 100;
            var spacingWidth = cardWidth * 0.1;
            var numberOfCards = result.length;            
            var dialogWidth = (cardWidth + spacingWidth) * numberOfCards + 4 * spacingWidth;

            
            var aspectRatio = 1.5;
            var cardHeight = cardWidth * aspectRatio;
            var overlap = cardHeight * 0.2;
            var dialogHeight = cardHeight + (overlap + 15) * numberOfCards;
            
            var dialog = $("<div id='modal'></div>").dialog(
                    { 
                      modal: true,
                      dialogClass: "no-close",
                      resizable: true,
                      width: `${dialogWidth}`,
                      height: `${dialogHeight}`
                    }
            );
            for(var i = 0; i < result.length; i++) {
                for(var k = 0; k <= i; k++) {
                    var div = getNewCard(result[k]);
                    $("#modal").append(div);
                    div.css(getCSS());
                    div.on("click", [i+1], function(event) { // need a copy of the closure i
                        var howManyCards = event.data[0];
                        result = result.slice(0, howManyCards);
                        deferred.resolve(result);
                        $("#modal").dialog("destroy");
                    });
                }
            }
        }

        function doSingleCardSequence() {
        // if stacks are not empty dragTop and dropTop must differ by one
        // bank stacks check suit as well as pip value
            if(dropStack.type === "bank") {
                var inSequence = dragStack.getInSequence()
                if(dropStack.isEmpty()) {
                    if(pip(dragTop) === 1) result = inSequence;
                } else {
                    if(dragTop%52 - dropTop%52 === 1) result = inSequence;
                }
            }
            if(dropStack.type === "table") {
                if(dropStack.isEmpty()) {
                    result = up;
                } else {
                    if(pip(dropTop) - pip(dragTop) === 1) result = up;
                }
            }
            deferred.resolve(result);
        }

        function doUpSequence() {
            // up sequences: e.g. up = [9 8 7] (array stored backwards)
            //     a) transfer to empty stack
            //          all cards can be transferred
            //     b) transfer between populated stacks
            //          all cards can be transferred
            //     c) transfer to bank
            //          only 1 card can be transferred
            if(dropStack.type === "table") {
                if(dropStack.isEmpty()) {
                    result = up;
                } else {
                    if(pip(dropTop) - pip(dragTop) === 1) {
                        result = up;
                    }
                }
            }
            if(dropStack.type === "bank") {
                if(dropStack.isEmpty()) {
                    if(pip(dropTop) === 1) result = [dragTop];
                } else {
                    if(dragTop%52 - dropTop%52 === 1) {
                        result = [dragTop];
                    }
                }
            }
            if(result.length > 1) {
                promptForCards(result);
            } else {
                deferred.resolve(result);                
            }
        }

        function doDownSequence() {
            // down sequences: e.g. down = [7 8 9 10] (array stored backwards)
            //     a) transfer to empty stack
            //          1 card  if 1 empty stacks
            //          2 cards if 2 empty stacks
            //          4 cards if 3 empty stacks
            //          2**(N-1) cards if N empty stacks
            //     b) transfer between populated stacks
            //          1 card  if 0 empty stacks
            //          2 cards if 1 empty stacks
            //          4 cards if 2 empty stacks
            //          2**N cards if N empty stacks
            //     c) transfer to bank
            //          all cards can be transferred

            if(dropStack.type === "table") {
                if(dropStack.isEmpty()) {
                    var maxCardsCanMove = Math.pow(2, emptyStacks-1);
                    result = down.slice(0, maxCardsCanMove);
                    if(result.length > 1) {
                        promptForCards(result);
                        return;
                    }
                } else {
                    var maxCardsCanMove = Math.pow(2, emptyStacks);
                    var reducedDown = down.slice(0, maxCardsCanMove);
                    var downPips = pips(reducedDown);
                    var dragTopIndex = downPips.indexOf(pip(dropTop)-1);
                    if(pip(dropTop) - downPips[dragTopIndex] === 1) {
                        result = down.slice(0, dragTopIndex+1);
                    }
                }
            }
            if(dropStack.type === "bank") {
                var cards = dragStack.getInSequence();
                if(dropStack.isEmpty()) {
                    if(pip(cards[0]) === 1) result = cards;
                } else {
                    if(dragTop%52 - dropTop%52 === 1) result = cards;
                }
                if(result.length > 1) {
                    promptForCards(result);
                    return;
                }
            }
            deferred.resolve(result);
        }
        var deferred = jQuery.Deferred();
        var result = [];
        var dropStack = this;
        var dropTop = dropStack.getTop();
        var dragTop = dragStack.getTop();
        var emptyStacks = Stack.howManyEmptyStacks();
        
        dragStack.compute();
        
        var up = dragStack.getUp();
        var down = dragStack.getDown();
        var sequence = getSequence();
        if(sequence === 0) doSingleCardSequence(up);
        if(sequence > 0) doUpSequence(up); 
        if(sequence < 0) doDownSequence(down);
        return deferred.promise();
    }

    constructor(id, index, type) {
        this.id = id;
        this.type = type;
        this.index = index;
        this.cards = [];
        this.up = [];
        this.down = [];
        this.inSequence = [];
    }

    static find(searchType, searchId) {
        var result;
        for(var i = 0; i < stacks.length; i++) {
            var type = stacks[i].type;
            var id = stacks[i].id;
            if(searchType === type && searchId === id) {
                result = stacks[i];
                break;
            } 
        }
        return result;
    }
    
    findCard(div) {
        var position = -1;
        var card = div.data("card-info").cardIndex;
        for(var i = 0; i < this.length(); i++) {
            if(this.cards[i] === card) {
                position = i;
                break;
            }
        }
        return position;
    }
    
    compute() {
        // up: [x x 3 4 5] is stored as [5 4 3] (working from top)
        // down: [ x x 6 5 4] is stored as [4 5 6] (working from top)
        // inSequence: like down, but must be all the same suit
        function buildSequence(array, comparator) {
            var top = stack.getTop();
            array.push(top);
            for(var i = cards.length - 2;  i >= 0; i--) {
                var next = cards[i];
                if(cardIsFaceDown(next)) break;
                if(!comparator(next, top)) break;
                top = next;
                array.push(top);
            }                        
        }
        var stack = this;
        var cards = this.cards;        
        this.up = [];
        this.down = [];
        this.inSequence = [];
        buildSequence(this.up, function(a,b){ return pip(b) - pip(a) === 1})
        buildSequence(this.down, function(a,b){ return pip(a) - pip(b) === 1})
        buildSequence(this.inSequence, function(a,b){ return a%52 - b%52 === 1})
        var stack = this;
    }
    
    getTop() {
        return this.cards[this.cards.length - 1];
    }
    
    length() {
        return this.cards.length;        
    }

    isStackEmpty() {
        return this.length() === 0;
    }
    
    push(card) {
        this.cards.push(card);
        var div = DOM[card];
        div.data("card-info", 
        { 
            stackIndex: this.index,
            cardIndex: card
        });
        makeDraggable(div);
        makeDroppable(div);        
    }
    
    resetDragAndDrop() {
        var stack = this;
        // disable drag and drop on all but last card
        for(var i = 0; i < stack.cards.length; i++) {
            var card = stack.cards[i];
            var div = DOM[card];
            div.draggable("disable");
            div.droppable("disable");
        }
        // make last card drag and droppable
        if(!stack.isStackEmpty() && stack.type === "table") {
            var top = stack.getTop();
            var div = DOM[top];
            div.draggable("enable");
            div.droppable("enable");
        }
    }

    getInSequence() {
        return this.inSequence;    
    }
    
    getUp() {
        return this.up;    
    }
    
    getDown() {
        return this.down;    
    }
    
    isEmpty() {
        return this.length() === 0;    
    }
    
    removeClickHandler() {
        if(this.type === "pack") {
            var packStack = this;
            for(var i = 0; i < this.cards.length; i++) {
                var card = this.cards[i];
                var div = DOM[card];
                div.off("click");
            }
        }        
    }
    
    addClickHandler() {
        // add click handler to top of pack
        var packStack = this;
        var top = packStack.getTop();
        var div = DOM[top];
        div.click(packStack, packClickHandler);
    }
}
