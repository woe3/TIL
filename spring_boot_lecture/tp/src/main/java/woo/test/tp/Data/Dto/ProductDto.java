package woo.test.tp.Data.Dto;

import lombok.*;
import woo.test.tp.Data.entity.ProductEntity;

@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Builder
public class ProductDto {

    private String productId;
    private String productName;
    private int productPrice;
    private int productStock;

    public ProductEntity toEntity() {
        return ProductEntity.builder()
                .build(productId)
                .build();

    }

}
