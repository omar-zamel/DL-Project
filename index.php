<!DOCTYPE html>
<html lang="ar" dir="rtl" xmlns="http://www.w3.org/1999/xhtml">

<head>

    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dlalat دلالات</title>
    <!-- Bootstrap Styles-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FontAwesome Styles-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
    <!-- Morris Chart Styles-->
    <link href="assets/js/morris/morris-0.4.3.min.css" rel="stylesheet" />
    <!-- Custom Styles-->
    <link href="assets/css/custom-styles.css" rel="stylesheet" />
    <!-- Google Fonts-->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
	
	  		    <link rel="shortcut icon" href="images/logo2.png"/>


<style>
@font-face {
   font-family: myFirstFont;
   src: url(fonts/NotoKufiArabic-Regular.ttf);
   font-size:8px;
}
body {
   font-family: myFirstFont;
}

</style>
</head>

<body >
    <div id="wrapper">
        <nav class="navbar navbar-default top-navbar" role="navigation">

                                 <center> <a class="navbar-brand" href="index.php">Dlalat دلالات</a>

            
        </nav>

        <div id="page-wrapper" >
            <div id="page-inner">


                <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-header">
                           <Center><img src="images/logo.png" width="15%"/>
Dlalat دلالات <img src="images/logo.png" width="15%"/>

                        </h1>
					
                    </div>
                </div>
				
				
                <!-- /. ROW  -->

              
				
				<div class="row">
				<div class="col-md-12">
					<div class="panel panel-default">
						<div class="panel-heading">
						<center>
 أدخل سؤالك باللغة العربية

  </div>
						<div class="panel-body">

<center>




 <form action="#" method="post">
 
 
  <div class="form-group">
                                            <label>السؤال</label>
  
                                                 <input type="text" name="question" id="question"  class="form-control" required>

                                        </div>
										
										
							 <div class="form-group">
  										        <input type="submit" class="btn btn-primary" value="اسأل">


                                        </div>			
       
	
										
                                     
                                       
										

                                    </form>
									
									
									
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $question = $_POST['question'];
    $filePath = "data-model-result.jsonl";
    if (!file_exists($filePath)) {
        die("The JSON file was not found.");
    }
    // Call the Python script with the user question
    $pythonScriptPath = "preprocess_question1.py";
    $command = "python3 $pythonScriptPath " . escapeshellarg($question);
    $preprocessedQuestion = shell_exec($command);
    // Decode the JSON output from the Python script
    $decodedAnswers = json_decode($preprocessedQuestion, true);
	echo " السؤال: " . $question . "<br>";
    // Check if decoding was successful
    if (empty($decodedAnswers)) {
        die("Error decoding JSON output from Python script.");
    }
    // Check if the Python script found any answers
    if (empty($decodedAnswers['results'])) {
        // If no answers were found, proceed to the API section
        $api_key = "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";
        $openai_api_url = "https://api.openai.com/v1/chat/completions";
        $headers = [
            "Content-Type: application/json",
            "Authorization: Bearer $api_key",
        ];
        // API request for the first question
		$question2 = $question . ' والدليل الشرعي على ذلك';
        $data = [
            "model" => "gpt-3.5-turbo",
            "messages" => [
                ["role" => "system", "content" => "You are a helpful assistant."],
                ["role" => "user", "content" => $question2],
            ],
        ];
        $curl = curl_init($openai_api_url);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
        $api_response = curl_exec($curl);
        curl_close($curl);
        $api_response = json_decode($api_response, true);
        echo $api_answer = $api_response["choices"][0]["message"]["content"];

    } else {
        // Display the unique answers from Python script

        foreach ($decodedAnswers['results'] as $answer) {
            echo "<div style='background-color: #FFFFE0; padding: 5px; margin-bottom: 10px;'>";
            echo "<b>۞</b> " . str_replace($answer['text'], '<span style="color: red;">' . $answer['text'] . '</span>', $answer['passage']) . "<br>";
            echo "</div>";
        }
    }
}
?>
	

<hr>



	
									
									
</center>

						</div>
					</div>  
					</div>		
				</div> 	
				
               
                <!-- /. ROW  -->

	   
		
		
			
				
				
				
				
               
                <!-- /. ROW  -->
				<footer><center><p>دلالات Dlalat  © 2023. جميع الحقوق محفوظة </p></center></footer>
            </div>
            <!-- /. PAGE INNER  -->
        </div>
        <!-- /. PAGE WRAPPER  -->
    </div>
    <!-- /. WRAPPER  -->
    <!-- JS Scripts-->
    <!-- jQuery Js -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!-- Bootstrap Js -->
    <script src="assets/js/bootstrap.min.js"></script>
	 
    <!-- Metis Menu Js -->
    <script src="assets/js/jquery.metisMenu.js"></script>
    <!-- Morris Chart Js -->
    <script src="assets/js/morris/raphael-2.1.0.min.js"></script>
    <script src="assets/js/morris/morris.js"></script>
	
	
	<script src="assets/js/easypiechart.js"></script>
	<script src="assets/js/easypiechart-data.js"></script>
	
	
    <!-- Custom Js -->
    <script src="assets/js/custom-scripts.js"></script>


</body>

</html>