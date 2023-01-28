package hello_company_name.hello_spring_project_name.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public  String home(){
        return "home";
    }
}
