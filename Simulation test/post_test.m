url    = 'http://localhost/xampp/FYP/test_post.php';
number1 = 89;
number2 = 2;
%params = {'number1' ,'number1' ,'number2' ,'number2'};
%[paramString,header] = http_paramsToString(params);


paramstring =  strcat('number1=',num2str(number1),'&','number2=',num2str(number2));
[output,extras] = urlread2(url,'POST',paramString,header);





 