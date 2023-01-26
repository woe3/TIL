package hello_company_name.hello_spring_project_name;

import hello_company_name.hello_spring_project_name.repository.MemberRepository;
import hello_company_name.hello_spring_project_name.repository.MemoryMemberRepository;
import hello_company_name.hello_spring_project_name.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}
