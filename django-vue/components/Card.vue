<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-1by1">
                <img
                    :src="thumbnailPhotoId"
                    width="500"
                    height="500"
                    alt="Placeholder image"
                />
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="title is-4">{{ title }}</p>
                </div>
            </div>

            <div class="content">
                <small v-if="priceWas" class="has-text-grey-light"
                    >de R$
                    {{ priceWas.toFixed(2).replace('.', ',') }} por</small
                >
                <br />
                <strong
                    >R$ {{ (price * 0.9).toFixed(2).replace('.', ',') }} à
                    vista</strong
                >
                <br />
                <small>ou R$ {{ price.toFixed(2).replace('.', ',') }} em</small>
                <br />
                <small
                    >10x de R$
                    {{ (price / 10).toFixed(2).replace('.', ',') }} sem
                    juros</small
                >
            </div>
            <div class="card-footer">
                <b-button type="is-primary" expanded>Ver</b-button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Card',
    props: {
        title: {
            type: String,
            required: true
        },
        price: {
            type: Number,
            required: true
        },
        priceWas: {
            type: Number,
            required: false,
            default: null
        },
        thumbnailPhotoId: {
            type: String,
            required: true
        }
    }
}
</script>
