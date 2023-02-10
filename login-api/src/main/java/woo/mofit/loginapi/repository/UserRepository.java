package woo.mofit.loginapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import woo.mofit.loginapi.model.User;

// JpaRepository 를 상속하면 자동 컴포넌트 스캔됨.
public interface UserRepository extends JpaRepository<User, Integer> {
    //findBy 규칙 -> Username 문법
    // select * from user where username = ?(username)
    public User findByUserID(String userID); //jpa 쿼리 메서드

}
