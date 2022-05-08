<template lang='pug'>

div.buttongroup-container
    label(v-if="label" class="label") {{ label }}
    div.buttongroup(:class="{'buttongroup--disabled': this.disabled}")
        button(v-for="item in items"
            :class="buttonClasses(item.id)"
            :disabled="disabled"
            :key="item.id" 
            @click="emit(item)") {{ item.name }}
        slot

</template>


<script>
import { log } from 'util';
export default {
    name: "ButtonGroup",
    props: {
        items: { type: Array, default: () => [] },  // needs to be [{'name': xxx, 'id': yyy}, ...]
        disabled: { type: Boolean, default: false },
        value: { type: [String, Object] },  // value that gets emitted to the outside
        label: { type: String, default: "" },
    },
    data() {
        return {};
    },
    methods: {
        emit(item) {
            if (typeof(this.value) === 'string')
                this.$emit('input', item.id);
            else if (typeof(this.value) === 'object')
                console.log(item);
                this.$emit('input', item);
        },
        buttonClasses(id) {
            let focussed;
            if (typeof(this.value) === 'string')
                focussed = this.value == id;
            else if (typeof(this.value) === 'object')
                focussed = this.value.id == id;

            return {
                "disabled": this.disabled,
                "focus": focussed
            };
        },
    },
    beforeMount() {},
};
</script>


<style lang="scss" scoped>

// --primary-color: blue;
// --muted-font-color: gray;

label {
    width: 100%;
    display: block;
    margin-left: 3px;
    margin-bottom: 2px;
    font-family: inherit;
    font-size: 0.8rem;
    line-height: 17px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: gray;
}

.buttongroup {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: stretch;
    // margin-right: 5px;
    border: 1px solid gray;
    // border-radius: 2px;
    // box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12), inset 0 1px 2px rgba(0, 0, 0, 0.2);

    &.disabled {
        pointer-events: none;
        cursor: not-allowed;
    }

    button {
        height: calc(30px - 2px);
        flex: 1 1 0;
        margin: 0;
        outline: none;
        font-family: inherit;
        font-size: inherit;
        border-width: 0;
        background-color: whitesmoke;
        padding: 0 10px;
        color: darkslategray;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        white-space: nowrap;

        &.disabled {
            box-shadow: none;
            color: lightgrey;
            background-color: silver;
            border-color: silver;
        }

        &:hover {
            // background-color: var(--secondary-blue);
            color: lightgray;
        }

        &:active {
            background-color: rgba(blue, 0.3);
            color: darkslategray;
        }

        &.focus {
            background-color: gray;
            color: white;

            &:hover {
                background-color: darkgray;
                color: white;
            }
        }
    }
}
</style>