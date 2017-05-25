function recordAnswer(id, selection) {	
	var isCorrect = 0;
	var correctAnswer = '';
	
	// Get the correct answer
	$.post({
		url: "/getCorrectAnswer",
		data: { 'question_id': id},
		async: false,
		success: function(response) {
            correctAnswer = response;
		}
	});
	
	if (selection == correctAnswer) {
		isCorrect = 1;
		$("#resultMessage").html("Correct!");	
		$("#resultImage").attr('src', '/static/images/correct-web.png');
	}
	else {
		$("#resultMessage").html("Incorrect! <br/>The correct answer is " + correctAnswer + ".");
		$("#resultImage").attr('src', '/static/images/wrong-web.png');
	}
		
	// Record 
	$.post({
		url: "/save",
		data: { 'question_id': id, 'isCorrect': isCorrect },
		async: false
	});
	
	$( "#dialog-message").dialog( "open" );
}		