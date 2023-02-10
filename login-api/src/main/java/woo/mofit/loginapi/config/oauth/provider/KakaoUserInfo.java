package woo.mofit.loginapi.config.oauth.provider;

import java.util.Map;

public class KakaoUserInfo implements OAuth2UserInfo{

    private Map<String, Object> attributes;
    private Map<String, Object> attributesAccount;
    private Map<String, Object> attributesProfile;

    public KakaoUserInfo(Map<String, Object> attributes) {
        this.attributes = attributes;
        this.attributesAccount = (Map<String, Object>) attributes.get("kakao_account");
        this.attributesProfile = (Map<String, Object>) attributesAccount.get("profile");
    }

    @Override
    public String getProviderId() {
        return String.valueOf(attributes.get("id"));
    }

    @Override
    public String getPrivider() {
        return "kakao";
    }

    @Override
    public String getEmail() {
        return String.valueOf(attributesAccount.get("email"));
    }

    @Override
    public String getName() {
        return (String) attributesProfile.get("nickname");
    }
}
