<?php
        //phpinfo();
	header("Access-Control-Allow-Origin: *");
        echo shell_exec("sudo /home/pi/controleCatraca/destrava.py");
        echo json_encode(array("finalizado" => 1));
