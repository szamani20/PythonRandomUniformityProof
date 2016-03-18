import matplotlib.pyplot as plt
import numpy


def main():
    width = 750
    height = 750
    dpi = 72.0

    z = numpy.random.randint(0, 750, (width, height))

    size = numpy.array(z.shape)
    fig_size = size[1] / dpi, size[0] / dpi

    fig = plt.figure(figsize=fig_size)
    fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
    plt.imshow(z, interpolation='nearest', cmap=plt.cm.gray_r)
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()
