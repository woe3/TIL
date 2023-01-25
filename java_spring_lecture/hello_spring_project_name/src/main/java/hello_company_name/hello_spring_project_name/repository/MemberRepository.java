package hello_company_name.hello_spring_project_name.repository;

import hello_company_name.hello_spring_project_name.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();


}
