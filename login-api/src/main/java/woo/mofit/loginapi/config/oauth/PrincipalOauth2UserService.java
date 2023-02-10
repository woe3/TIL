package woo.mofit.loginapi.config.oauth;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;
import woo.mofit.loginapi.config.auth.PrincipalDetails;
import woo.mofit.loginapi.config.oauth.provider.GoogleUserInfo;
import woo.mofit.loginapi.config.oauth.provider.KakaoUserInfo;
import woo.mofit.loginapi.config.oauth.provider.NaverUserInfo;
import woo.mofit.loginapi.config.oauth.provider.OAuth2UserInfo;
import woo.mofit.loginapi.model.User;
import woo.mofit.loginapi.repository.UserRepository;

import java.util.Map;

@Service
public class PrincipalOauth2UserService extends DefaultOAuth2UserService {

    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;
    @Autowired
    private UserRepository userRepository;

    // 구글에서 받은 유저 데이터를 후처리하는 함수
    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        System.out.println("getClientRegistration : " + userRequest.getClientRegistration());
        System.out.println("getAccessToken : " + userRequest.getAccessToken().getTokenValue());
        OAuth2User oAuth2User = super.loadUser(userRequest);
        System.out.println("getAttributes : " + oAuth2User.getAttributes());

        OAuth2UserInfo oAuth2UserInfo = null;
        if (userRequest.getClientRegistration().getRegistrationId().equals("google")) {
            oAuth2UserInfo = new GoogleUserInfo(oAuth2User.getAttributes());
        }
        else if(userRequest.getClientRegistration().getRegistrationId().equals("naver")){
            oAuth2UserInfo = new NaverUserInfo((Map)oAuth2User.getAttributes().get("response"));
        }
        else if(userRequest.getClientRegistration().getRegistrationId().equals("kakao")){
            oAuth2UserInfo = new KakaoUserInfo(oAuth2User.getAttributes());
        }


        String provider = oAuth2UserInfo.getPrivider(); // google

        String providerId =oAuth2UserInfo.getProviderId();
        System.out.println(providerId);
        String userID = provider + "_" + providerId;
        String password = bCryptPasswordEncoder.encode("GetInThere");
        String email = oAuth2UserInfo.getEmail();
        String role = "ROLE_USER";
        String name = oAuth2UserInfo.getName();

        User userEntity = userRepository.findByUserID(userID);

        if(userEntity == null) {
            userEntity = User.builder()
                    .userID(userID)
                    .password(password)
                    .email(email)
                    .role(role)
                    .provider(provider)
                    .providerId(providerId)
                    .name(name)
                    .build();
            userRepository.save(userEntity);
        }

        return new PrincipalDetails(userEntity, oAuth2User.getAttributes());
    }
}
