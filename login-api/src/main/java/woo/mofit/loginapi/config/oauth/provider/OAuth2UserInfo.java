package woo.mofit.loginapi.config.oauth.provider;

public interface OAuth2UserInfo {
    String getProviderId();
    String getPrivider();
    String getEmail();
    String getName();
}
