package woo.mofit.loginapi.contorller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import woo.mofit.loginapi.config.auth.PrincipalDetails;
import woo.mofit.loginapi.model.User;
import woo.mofit.loginapi.repository.UserRepository;

@RestController
public class IndexController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;


    @GetMapping({ "", "/" })
    public String index() {
        return "index";
    }
    // 로그인 페이지
    @GetMapping("/login")
    public String loginFrom() {
        return "login";
    }
    // 가입 페이지
    @GetMapping("/join")
    public String joinForm() {
        return "join";
    }

    @PostMapping("/joinProc")
    public String join(User user) {
        user.setRole("ROLE_USER");
        String rawPassword = user.getPassword();
        String encPassword = bCryptPasswordEncoder.encode(rawPassword);
        user.setPassword(encPassword);
        userRepository.save(user);
        System.out.println(user);
        return "redirect:/login";
    }

    @GetMapping("/admin")
    public @ResponseBody String admin() {
        return "admin";
    }

    @GetMapping("/userinfo")
    public @ResponseBody String userInfo(@AuthenticationPrincipal PrincipalDetails principalDetails) {
        System.out.println("principalDetails"+principalDetails.getUser());
        return "userinfo";
    }


}
