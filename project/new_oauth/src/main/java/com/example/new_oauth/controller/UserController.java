package com.example.new_oauth.controller;

import com.example.new_oauth.auth.PrincipalDetails;
import com.example.new_oauth.domain.Role;
import com.example.new_oauth.domain.User;
import com.example.new_oauth.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class UserController {
    @Autowired private UserRepository userRepository;
    @Autowired private BCryptPasswordEncoder bCryptPasswordEncoder;

    @GetMapping("/loginForm")
    public String loginForm(){
        return "login";
    }

    @GetMapping("/joinForm")
    public String joinForm(){
        return "join";
    }

    @PostMapping("/join")
    public String join(@ModelAttribute User user){
        user.setRole(Role.ROLE_USER);

        String encodePwd = bCryptPasswordEncoder.encode(user.getPassword());
        user.setPassword(encodePwd);

        userRepository.save(user);  //반드시 패스워드 암호화해야함
        return "redirect:/loginForm";
    }

    @GetMapping("/user")
    @ResponseBody
    public String user(){
        return "user";
    }

    @GetMapping("/manager")
    @ResponseBody
    public String manager(){
        return "manager";
    }

    @GetMapping("/admin")
    @ResponseBody
    public String admin(){
        return "admin";
    }


    // !!!! OAuth로 로그인 시 이 방식대로 하면 CastException 발생함
    @GetMapping("/form/loginInfo")
    @ResponseBody
    public String formLoginInfo(Authentication authentication, @AuthenticationPrincipal PrincipalDetails principalDetails){

        PrincipalDetails principal = (PrincipalDetails) authentication.getPrincipal();
        User user = principal.getUser();
        System.out.println(user);
        //User(id=2, username=11, password=$2a$10$m/1Alpm180jjsBpYReeml.AzvGlx/Djg4Z9/JDZYz8TJF1qUKd1fW, email=11@11, role=ROLE_USER, createTime=2022-01-30 19:07:43.213, provider=null, providerId=null)

        User user1 = principalDetails.getUser();
        System.out.println(user1);
        //User(id=2, username=11, password=$2a$10$m/1Alpm180jjsBpYReeml.AzvGlx/Djg4Z9/JDZYz8TJF1qUKd1fW, email=11@11, role=ROLE_USER, createTime=2022-01-30 19:07:43.213, provider=null, providerId=null)
        //user == user1

        return user.toString();
    }

}