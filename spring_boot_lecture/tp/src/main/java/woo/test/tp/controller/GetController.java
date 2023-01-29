package woo.test.tp.controller;

import org.springframework.web.bind.annotation.*;
import woo.test.tp.DTO.MemberDTO;

import java.util.Map;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {
    // http://localhost:8080/api/v1/get-api/hello
    @RequestMapping(value = "/hello", method = RequestMethod.GET)
    public String getHello() {
        return  "Hello World!";
    }
    // http://localhost:8080/api/v1/get-api/name
    @GetMapping(value = "/name")
    public String getName() {
        return "WOO";
    }
    // http://localhost:8080/api/v1/get-api/variable1/Fucking-spring
    @GetMapping(value = "/variable1/{variable}")
    public String getVariable1(@PathVariable String variable) {
        return variable;
    }
    // http://localhost:8080/api/v1/get-api/variable2/Fucking-spring
    @GetMapping(value = "variable2/{variable}")
    public String getVariable2(@PathVariable("variable") String var) {
        return var;
    }
    // http://localhost:8080/api/v1/get-api/request1?name=woo&gender=male&age=23
    @GetMapping(value = "/request1")
    public String getRequestParam1(
            @RequestParam String name,
            @RequestParam String gender,
            @RequestParam String age) {
        return name + " " + gender + " " + age;
    }
    // http://localhost:8080/api/v1/get-api/request2?name=woo&gender=male&age=23
    @GetMapping(value = "/request2")
    public  String getRequestParam2(@RequestParam Map<String, String> param) {
        StringBuilder sb = new StringBuilder();

        param.entrySet().forEach(map -> {
            sb.append(map.getKey() + " : " + map.getValue() + "\n");
        });
        return sb.toString();
    }
    // http://localhost:8080/api/v1/get-api/request3?name=woo&gender=male&age=23
    @GetMapping(value = "/request3")
    public String getRequestParam3(MemberDTO memberDTO) {
        return memberDTO.toString();
    }
}