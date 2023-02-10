package woo.mofit.loginapi.config.auth;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import woo.mofit.loginapi.model.User;
import woo.mofit.loginapi.repository.UserRepository;

// 시큐리티 설정에서 로그인 요청이오면 자동으로 유저디테일서비스 탑으로  IOC 되어있는 오드유저바이유저네임 함수가 실행
@Service
public class PrincipalDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override // 프론트에서 포스트 받을 때 "username"으로 제대로 받야한다.
    public UserDetails loadUserByUsername(String userID) throws UsernameNotFoundException {
        User userEntity = userRepository.findByUserID(userID);
        if(userEntity != null) {
            return new PrincipalDetails(userEntity);
        }
        return null;
    }

}
